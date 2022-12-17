import pickle
import numpy as np

from apps.content.models import Post
from apps.recommend.conf import SAVED_MODEL_DIRECTORY, SAVED_DATASET_DIRECTORY, SAVED_ITEM_SIMILARITY_MATRIX_DIRECTORY


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


def get_top_k_known_positive_items_ids(user_id, top_k, interactions, user_id_map, item_id_map):

    # use tocsr function to iterate spares matrix
    known_positives_model_ids = [interactions.tocsr()[list(user_id_map).index(user_id)].indices]

    # mapping to item ids
    known_positives_ids = [int(list(item_id_map)[item_model_id])
                           for item_model_id in known_positives_model_ids[0]][0:top_k]

    return known_positives_ids


def get_top_k_items_ids(user_id, top_k, model, interactions, user_id_map, item_id_map):
    n_users, n_items = interactions.shape
    scores = model.predict(user_id_map[user_id], np.arange(n_items))
    top_items_model_ids = np.argsort(-scores)[:top_k]
    top_items_ids = [int(list(item_id_map)[item_model_id]) for item_model_id in top_items_model_ids]
    return top_items_ids


def load_item_similarity_matrix():
    with open(f'{SAVED_ITEM_SIMILARITY_MATRIX_DIRECTORY}/item_similarity_matrix.pickle', 'rb') as file:
        loaded_item_similarity_matrix = pickle.load(file)
    return loaded_item_similarity_matrix


def get_top_k_similar_items(item_id, top_k):

    dataset = load_dataset()
    user_id_map, item_id_map = get_id_mapping(dataset)

    item_similarities_matrix = load_item_similarity_matrix()

    similar_items_model_ids = np.argsort(
        -item_similarities_matrix[list(item_id_map.keys()).index(item_id)])[0:top_k + 1]
    top_k_similar_items_ids = [list(item_id_map)[item_model_id] for item_model_id in similar_items_model_ids]
    top_k_similar_items = Post.objects.get_posts_by_ids(id_list=top_k_similar_items_ids)
    return top_k_similar_items
