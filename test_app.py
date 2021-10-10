from app import app


def test_list_status():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_edit_status():
    response = app.test_client().get('/edit')
    assert response.status_code == 200


def test_add_todo():
    response = app.test_client().get('/edit')
    assert b'To Do App' in response.data
    assert b'Todo Title' in response.data
    assert b'Add' in response.data
