# TODO  Dont work!
#class SignalUserCreateTest(TestCase):
#    def setUp(self):
#        self.user = User.objects.create_user(username='testuser123', password='testpass123', is_staff=True)
#        self.user.save()
#
#    def test_create_user_signal(self):
#        self.assertTrue(Profile.objects.filter(user=self.user))
