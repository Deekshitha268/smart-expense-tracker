def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_add_expense(client):
    response = client.post(
        "/expenses",
        json={
            "title": "Groceries",
            "amount": 500,
            "category": "Food",
            "date": "2026-07-31"
        }
    )

    assert response.status_code == 201


def test_get_all_expenses(client):
    response = client.get("/expenses")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_filter_by_category(client):
    response = client.get("/expenses?category=Food")

    assert response.status_code == 200


def test_total_expenses(client):
    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert "total" in response.get_json()


def test_total_by_category(client):
    response = client.get("/expenses/total?category=Food")

    assert response.status_code == 200

    data = response.get_json()

    assert "category" in data
    assert "total" in data


def test_delete_expense(client):
    response = client.delete("/expenses/1")

    assert response.status_code in [200, 404]


def test_invalid_expense(client):
    response = client.post(
        "/expenses",
        json={
            "title": "",
            "amount": -100,
            "category": "",
            "date": ""
        }
    )

    assert response.status_code == 400