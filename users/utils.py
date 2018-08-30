def user_media_path(obj, filename):
    return f"users/{obj.id}/avatar/{filename}/"

def user_media_cover_path(obj, filename):
  return f"users/{obj.id}/cover/{filename}/"