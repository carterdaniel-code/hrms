"""
horilla/horilla_backends_gcp.py
"""

from storages.backends.gcloud import GoogleCloudStorage

from horilla import settings


class PrivateMediaStorage(GoogleCloudStorage):
    """
    PrivateMediaStorage
    """

    # Privacy is controlled with bucket IAM. Avoiding per-object ACLs also makes
    # this backend compatible with GCS Uniform Bucket-Level Access.
    location = settings.env("GCS_MEDIA_PREFIX", default="media")
    default_acl = None
    file_overwrite = False
