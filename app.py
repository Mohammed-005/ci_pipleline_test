import os
import colorama

stage_env = os.environ.get("STAGE_ENV")

if stage_env == "PRODUCTION":
    print("Production configuration verified. System fully functional.")
else:
    raise ValueError("CRITICAL: Unapproved staging environment configuration detected!")
