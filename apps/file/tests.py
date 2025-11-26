from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from rest_framework import status

from apps.file.models import File


class FileViewSetTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.existing_file = File.objects.create(
            file=SimpleUploadedFile("test.txt", b"hello world")
        )

    def test_list_files(self):
        response = self.client.get("/file/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_file(self):
        response = self.client.get(f"/file/{self.existing_file.id}/")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data["id"]), str(self.existing_file.id))

    def test_create_file(self):
        new_file = SimpleUploadedFile("new.txt", b"new content")

        response = self.client.post(
            "/file/",
            {"file": new_file},
            format="multipart"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(File.objects.count(), 2)

    def test_update_file(self):
        updated_file = SimpleUploadedFile("updated.txt", b"updated content")

        response = self.client.put(
            f"/file/{self.existing_file.id}/",
            {"file": updated_file},
            format="multipart"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated = File.objects.get(id=self.existing_file.id)
        self.assertTrue(updated.file.name.endswith("updated.txt"))

    def test_delete_file(self):
        response = self.client.delete(f"/file/{self.existing_file.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(File.objects.count(), 0)
