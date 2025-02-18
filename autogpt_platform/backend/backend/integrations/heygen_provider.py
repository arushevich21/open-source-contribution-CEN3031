import requests
import os


class HeyGenProvider:
    """Handles interactions with the HeyGen API to generate avatar videos."""

    API_URL = "https://api.heygen.com/v2/video.create"
    API_KEY = os.getenv("HEYGEN_API_KEY")  # Securely load API key

    @classmethod
    def create_avatar_video(cls, avatar_id, voice_id, text, background="default"):
        """
        Calls HeyGen API to generate an avatar video.

        :param avatar_id: ID of the avatar to use.
        :param voice_id: ID of the voice for narration.
        :param text: Text content for the avatar to say.s
        :param background: Background style (optional).
        :return: JSON response from HeyGen API.
        """
        if not cls.API_KEY:
            raise ValueError("HeyGen API Key is missing! Set HEYGEN_API_KEY in the environment.")

        headers = {
            "Authorization": f"Bearer {cls.API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "video_config": {
                "clips": [
                    {
                        "avatar_id": avatar_id,
                        "background": background,
                        "voice_id": voice_id,
                        "text": text
                    }
                ],
                "ratio": "16:9",
                "test": False
            }
        }

        response = requests.post(cls.API_URL, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
