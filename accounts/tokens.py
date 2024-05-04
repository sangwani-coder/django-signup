from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import int_to_base36, base36_to_int

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            str(user.pk) + str(timestamp) +
            str(user.profile.signup_confirmation)
        )

    def _make_token_with_timestamp(self, user, timestamp):
        ts_b36 = int_to_base36(timestamp)
        hash_value = self._make_hash_value(user, timestamp)
        return f"{hash_value}-{ts_b36}"

account_activation_token = AccountActivationTokenGenerator()
