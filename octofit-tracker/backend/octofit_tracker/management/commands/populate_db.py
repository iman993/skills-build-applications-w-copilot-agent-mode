from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):

        # Clear existing data (avoid bulk delete issues with Djongo)
        for model in [Activity, Leaderboard, User, Team, Workout]:
            for obj in model.objects.all():
                if getattr(obj, 'id', None):
                    obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create workouts
        run = Workout.objects.create(name='Running', description='Run fast!')
        lift = Workout.objects.create(name='Weight Lifting', description='Lift heavy!')

        # Create activities
        Activity.objects.create(user=users[0], workout=run, date=date.today(), duration_minutes=30, points=50)
        Activity.objects.create(user=users[1], workout=lift, date=date.today(), duration_minutes=45, points=70)
        Activity.objects.create(user=users[2], workout=run, date=date.today(), duration_minutes=25, points=40)
        Activity.objects.create(user=users[3], workout=lift, date=date.today(), duration_minutes=60, points=90)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, total_points=120)
        Leaderboard.objects.create(team=dc, total_points=130)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
