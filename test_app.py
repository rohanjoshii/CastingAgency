import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import create_app
from models import setup_db, Actor, Movie
import os


class CastingTestCase(unittest.TestCase):
    """This class represents the casting test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_test"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app)

        self.executive_producer_jwt = os.environ['EXECUTIVE_PRODUCER']

        self.new_movie = {
            'title': 'Title',
            'release_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        self.new_actor = {
            'name': 'Name',
            'age': 42,
            'gender': 'M'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation
    and for expected errors.
    """
    def test_get_actors(self):
        res = self.client().get('/actors', headers={
            "Authorization": "Bearer {}".format(self.executive_producer_jwt)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_get_movies(self):
        res = self.client().get('/movies', headers={
            "Authorization": "Bearer {}".format(self.executive_producer_jwt)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_delete_movie(self):
        movie = Movie(title='title', release_date='2020-09-02 11:11:57')
        movie.insert()
        movie_id = movie.id
        before = Movie.query.all()
        res = self.client().delete(f'/movies/{movie_id}', headers={
            "Authorization": "Bearer {}".format(self.executive_producer_jwt)})
        data = json.loads(res.data)
        after = Movie.query.all()
        movie = Movie.query.filter(Movie.id == movie.id).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], movie_id)
        self.assertTrue(len(before) - len(after) == 1)

    def test_422_delete_movie_failure(self):
        res = self.client().delete('/movies/1000', headers={
            "Authorization": "Bearer {}".format(self.executive_producer_jwt)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_add_movie(self):
        before = len(Movie.query.all())
        res = self.client().post('/movies', json=self.new_movie, headers={
            "Authorization": "Bearer {}".format(self.executive_producer_jwt)})
        data = json.loads(res.data)
        after = len(Movie.query.all())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue((after) - (before) == 1)

    def test_422_add_movie_failure(self):
        new_movie = {
            'title': 'title'
        }
        res = self.client().post('/movies', json=new_movie, headers={
            "Authorization": "Bearer {}".format(self.executive_producer_jwt)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable entity")

    def test_delete_actor(self):
        actor = Actor(name='name', age=32, gender='gender')
        actor.insert()
        actor_id = actor.id
        before = Actor.query.all()
        res = self.client().delete(f'/actors/{actor_id}', headers={
            "Authorization": "Bearer {}".format(self.executive_producer_jwt)})
        data = json.loads(res.data)
        after = Actor.query.all()
        actor = Actor.query.filter(Actor.id == actor.id).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], actor_id)
        self.assertTrue(len(before) - len(after) == 1)

    def test_422_delete_actor_failure(self):
        res = self.client().delete('/actors/1000', headers={
            "Authorization": "Bearer {}".format(self.executive_producer_jwt)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_add_actor(self):
        before = len(Actor.query.all())
        res = self.client().post('/actors', json=self.new_actor, headers={
            "Authorization": "Bearer {}".format(self.executive_producer_jwt)})
        data = json.loads(res.data)
        after = len(Actor.query.all())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue((after) - (before) == 1)

    def test_422_add_actor_failure(self):
        new_actor = {
            'name': 'name'
        }
        res = self.client().post('/actors', json=new_actor, headers={
            "Authorization": "Bearer {}".format(self.executive_producer_jwt)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable entity")

    def test_update_movie(self):
        res = self.client().patch('/movies/1', json={
            'title': 'title'
        }, headers={
            "Authorization": "Bearer {}".format(self.executive_producer_jwt)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["updated"])

    def test_422_update_movie_failure(self):
        res = self.client().patch('/movies/1', json=None, headers={
            "Authorization": "Bearer {}".format(self.executive_producer_jwt)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable entity")

    def test_update_actor(self):
        actor = Actor(name='name', age=32, gender='gender')
        actor.insert()
        actor_id = actor.id
        res = self.client().patch(f'/actors/{actor_id}', json={
            'name': 'name'
        }, headers={
            "Authorization": "Bearer {}".format(self.executive_producer_jwt)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["updated"])

    def test_422_update_actor_failure(self):
        res = self.client().patch('/actors/1', json=None, headers={
            "Authorization": "Bearer {}".format(self.executive_producer_jwt)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable entity")

"""
Make the tests conveniently executable
"""
if __name__ == "__main__":
    unittest.main()
