import requests
import json

def _fetch_custom_tdk(self, aweme_id):
    """
    Fetches custom TDK (Title, Description, Keywords) data from TikTok's API.
    This can include AI-generated summaries.

    Parameters
    ----------
    aweme_id : str or int
        The TikTok video ID (AWEME_ID)

    Returns
    -------
    str or None
        The AI summary text if available, otherwise None
    """
    try:
        url = f"https://www.tiktok.com/api/customtdk/item/?aid=1988&itemId={aweme_id}"

        response = self.request_and_retain_cookies(url)

        if response.status_code == 200:
            data = response.json()

            # Check if itemCustomTDK exists in the response
            if "itemCustomTDK" in data:
                item_custom_tdk = data["itemCustomTDK"]

                # Extract AI summary if it exists
                # The structure might vary, but typically it's in the description or a specific field
                ai_summary = item_custom_tdk

                if ai_summary:
                    self.log.info(f"--> Custom TDK AI summary found for video {aweme_id}")
                    return ai_summary
                else:
                    self.log.info(f"--> Custom TDK found but no AI summary for video {aweme_id}")
                    return None
            else:
                self.log.info(f"--> No custom TDK data available for video {aweme_id}")
                return None

        else:
            self.log.warning(f"--> Failed to fetch custom TDK data: HTTP {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        self.log.warning(f"--> Error fetching custom TDK data: {str(e)}")
        return None
    except json.JSONDecodeError as e:
        self.log.warning(f"--> Error parsing custom TDK JSON: {str(e)}")
        return None
    except Exception as e:
        self.log.warning(f"--> Unexpected error fetching custom TDK data: {str(e)}")
        return None
