from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.assertEqual(str(team), 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(email='batman@dc.com', name='Batman', team=team)
        self.assertEqual(str(user), 'batman@dc.com')

    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(email='spiderman@marvel.com', name='Spiderman', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2025-12-23')
        self.assertEqual(str(activity), 'spiderman@marvel.com - Running')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body workout')
        self.assertEqual(str(workout), 'Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(email='ironman@marvel.com', name='Ironman', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(str(leaderboard), 'ironman@marvel.com - Rank 1')
