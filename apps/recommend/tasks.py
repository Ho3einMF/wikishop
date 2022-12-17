from celery import shared_task

from apps.recommend.utils import load_model, load_dataset, get_id_mapping, load_interactions, \
    get_top_k_known_positive_items_ids, get_top_k_items_ids, get_top_k_similar_items_ids


#  This task just locks up for ids and passed to the view then in view operate select query for both item ids
@shared_task()
def get_item_user_recommend_ids(user_id, top_k):

    model = load_model()

    dataset = load_dataset()
    user_id_map, item_id_map = get_id_mapping(dataset)

    interactions = load_interactions()

    known_positives_items_ids = get_top_k_known_positive_items_ids(user_id=user_id,
                                                                   top_k=top_k,
                                                                   interactions=interactions,
                                                                   user_id_map=user_id_map,
                                                                   item_id_map=item_id_map)

    top_k_items_ids = get_top_k_items_ids(user_id=user_id, top_k=top_k,
                                          model=model, interactions=interactions,
                                          user_id_map=user_id_map, item_id_map=item_id_map)

    return known_positives_items_ids, top_k_items_ids


#  Similar above this task also return only ids of similar items and in view search by ids in database
@shared_task()
def get_item_item_recommend_ids(item_id, top_k):

    return get_top_k_similar_items_ids(item_id=item_id, top_k=top_k)
