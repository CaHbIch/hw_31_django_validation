import pytest


@pytest.mark.django_db
def test_ad_create(client, user, category):
    expected_response = {
        "id": user.pk,
        "image": None,
        "name": "Тест не менее 10 символов",
        "price": 2500,
        "author": None,
        "category": None,
        "is_published": False,
        "description": "Описание теста"
    }

    data = {
        "author_id": user.pk,
        "name": "Тест не менее 10 символов",
        "price": 2500,
        "description": "Описание теста",
        "is_published": False,
        "category_id": category.pk
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == expected_response

#
# @pytest.mark.django_db
# def test_ad_create_price_less_than_zero(client, user, category):
#     expected_response = {
#         "price": [
#             "Убедитесь, что это значение больше или равно 0."
#         ]
#     }
#
#     data = {
#         "author_id": user.pk,
#         "name": "Тест не менее 10 символов",
#         "price": -2,
#         "description": "Описание теста",
#         "is_published": False,
#         "category_id": category.pk
#     }
#
#     response = client.post(
#         "/ad/create/",
#         data,
#         content_type='application/json',
#     )
#
#     assert response.status_code == 400
#     assert response.data == expected_response
#
#
# @pytest.mark.django_db
# def test_ad_create_is_published_true(client, user, category):
#
#     expected_response = {
#         "is_published": [
#             "Это поле может быть неверным"
#         ]
#     }
#
#     data = {
#         "author_id": user.id,
#         "name": "Тест не менее 10 символов",
#         "price": 2500,
#         "description": "Описание теста",
#         "is_published": True,
#         "category_id": category.id
#     }
#
#     response = client.post(
#         "/ad/create/",
#         data,
#         content_type='application/json'
#     )
#
#     assert response.status_code == 400
#     assert response.data == expected_response
#
#
# @pytest.mark.django_db
# def test_ad_create_name_less_10_chars(client, user, category):
#
#     expected_response = {
#         "name": [
#             "Убедитесь, что это поле содержит не менее 10 символов."
#         ]
#     }
#
#     data = {
#         "author_id": user.id,
#         "name": "Test",
#         "price": 2500,
#         "description": "Описание теста",
#         "is_published": False,
#         "category_id": category.id
#     }
#
#     response = client.post(
#         "/ad/",
#         data,
#         content_type='application/json'
#     )
#
#     assert response.status_code == 400
#     assert response.data == expected_response
