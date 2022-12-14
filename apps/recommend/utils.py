import pickle
import numpy as np

from apps.content.models import Post
from apps.recommend.conf import SAVED_MODEL_DIRECTORY, SAVED_DATASET_DIRECTORY


def load_model():
    with open(f'{SAVED_MODEL_DIRECTORY}/model.pickle', 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model


def load_dataset():
    with open(f'{SAVED_DATASET_DIRECTORY}/dataset.pickle', 'rb') as file:
        loaded_dataset = pickle.load(file)
    return loaded_dataset


def load_interactions():
    with open(f'{SAVED_DATASET_DIRECTORY}/interactions.pickle', 'rb') as file:
        loaded_interactions = pickle.load(file)
    return loaded_interactions


def get_id_mapping(dataset):
    (user_id_map, user_feature_map, item_id_map, item_feature_map) = dataset.mapping()
    return user_id_map, item_id_map


def get_top_k_known_positive_items(user_id, top_k, interactions, user_id_map, item_id_map):

    # use tocsr function to iterate spares matrix
    known_positives_model_ids = [
        interactions.tocsr()[list(user_id_map).index(user_id)].indices]

    # mapping to item ids
    known_positives_ids = [list(item_id_map)[item_model_id] for item_model_id in known_positives_model_ids[0]][0:top_k]

    # find items by ids
    known_positive_items = Post.objects.get_posts_by_ids(id_list=known_positives_ids)

    return known_positive_items


def get_top_k_items(user_id, top_k, model, interactions, user_id_map, item_id_map):
    n_users, n_items = interactions.shape
    scores = model.predict(user_id_map[user_id], np.arange(n_items))
    top_items_model_ids = np.argsort(-scores)[:top_k]
    top_items_ids = [list(item_id_map)[item_model_id] for item_model_id in top_items_model_ids]
    top_items = Post.objects.get_posts_by_ids(id_list=top_items_ids)
    return top_items


def sample_recommendation(model, user_id, top_k):

    dataset = load_dataset()
    user_id_map, item_id_map = get_id_mapping(dataset)

    interactions = load_interactions()

    known_positives_items = get_top_k_known_positive_items(user_id=user_id,
                                                           top_k=top_k,
                                                           interactions=interactions,
                                                           user_id_map=user_id_map,
                                                           item_id_map=item_id_map)

    top_k_items = get_top_k_items(user_id=user_id, top_k=top_k,
                                  model=model, interactions=interactions,
                                  user_id_map=user_id_map, item_id_map=item_id_map)

    return known_positives_items, top_k_items
