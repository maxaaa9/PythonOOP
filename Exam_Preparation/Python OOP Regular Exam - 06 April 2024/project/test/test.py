from project.social_media import SocialMedia
from unittest import TestCase, main


class TestSocialMedia(TestCase):

    def setUp(self):
        self.test_media = SocialMedia("TV",
                                      "Instagram",
                                      100,
                                      "Testing")
        self.allowed_platform = ['Instagram', 'YouTube', 'Twitter']

    def test_init(self):
        self.assertEqual("TV", self.test_media._username)
        self.assertEqual("Instagram", self.test_media.platform)
        self.assertIsNone(self.test_media._validate_and_set_platform("Instagram"))
        self.assertEqual(100, self.test_media.followers)
        self.assertEqual("Testing", self.test_media._content_type)
        self.assertEqual([], self.test_media._posts)

    def test_negative_followers_value_raise_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.test_media.followers = -5

        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_invalid_platform_raise_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.test_media._validate_and_set_platform("Wrong")

        self.assertEqual(f"Platform should be one of {self.allowed_platform}",
                         str(ve.exception))

    def test_new_created_post_check_posts_append(self):
        result = self.test_media.create_post("News")
        expect = (f"New {self.test_media._content_type} post created by "
                  f"{self.test_media._username} on {self.test_media.platform}.")

        self.assertEqual(result, expect)
        self.assertEqual(1, len(self.test_media._posts))

    def test_like_post_with_invalid_index(self):
        result = self.test_media.like_post(-1)

        self.assertEqual(result, "Invalid post index.")

    def test_like_in_valid_interval_less_than_10_likes(self):
        self.test_media.create_post("Zero")
        self.test_media.create_post("One")
        self.test_media.create_post("two")
        test_index = 1

        result = self.test_media.like_post(test_index)
        self.assertEqual(1, self.test_media._posts[test_index]['likes'])
        self.assertEqual(result, f"Post liked by {self.test_media._username}.")

    def test_like_with_valid_index_on_post_with_more_than_10_likes(self):
        test_index = 0
        self.test_media.create_post("Zero")
        self.test_media._posts[test_index]['likes'] = 15

        result = self.test_media.like_post(test_index)

        self.assertEqual(result, f"Post has reached the maximum number of likes.")

    def test_comment_on_post_with_invalid_len_of_chars(self):
        invalid_comment = " "
        valid_index = 0
        self.test_media.create_post("HighNoon")

        result = self.test_media.comment_on_post(valid_index, invalid_comment)

        self.assertEqual(result, "Comment should be more than 10 characters.")

    def test_commend_on_valid_index_valid_comment_append_and_return(self):
        self.test_media.create_post("TesterExam")
        valid_index = 0
        valid_comment = "HardCoreTesterIsHere!"
        result = self.test_media.comment_on_post(valid_index, valid_comment)

        self.assertEqual(1, len(self.test_media._posts[valid_index]['comments']))
        self.assertEqual(result, f"Comment added by {self.test_media._username} on the post.")


if __name__ == "__main__":
    main()

