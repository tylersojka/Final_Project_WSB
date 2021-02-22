# import modin as pd
import boto3
import pandas as pd
import s3fs
import re
import logging
from botocore.exceptions import ClientError

# create paths to the uncleaned csv's 
post_path = "../Data/wallstreetbets_posts.csv"
comment_path = "../Data/wallstreetbets_comments.csv"

# Create a pandas df for each csv
comment_df = pd.read_csv(comment_path)
post_df = pd.read_csv(post_path)

# drop all rows that contained deleted data -- author and comment/post were deleted.
cleaned_df = comment_df[comment_df["author"] != "[deleted]"]
clean_post_df = post_df[post_df["author"] != "[deleted]"]

# create list of unwanted columns from the comment df
comment_garbage_columns = [
 'all_awardings', 
 'associated_award',
 'author_flair_background_color', # useless data
 'author_flair_css_class', # useless data
 'author_flair_richtext', # useless data
 'author_flair_template_id', # useless data
 'author_flair_text', # useless data
 'author_flair_text_color', # useless data
 'author_flair_type', # useless data
 'author_fullname', # useless data
 'author_patreon_flair', # useless data
 'author_premium', # useless data
 'awarders', # useless data
 'collapsed_because_crowd_control', # useless data
 'comment_type', # useless data
 'gildings', # useless data
 'is_submitter', # useless data
 'locked', # useless data
 'no_follow', # useless data
 'retrieved_on', # date this was added to pushshift, not useful
 'send_replies', # useless data
 'stickied', # useless data
 'subreddit', # only pulling from wsb, not helpful
 'subreddit_id', # only pulling from wsb, not helpful
 'top_awarded_type', # useless data
 'treatment_tags', # useless data
 'distinguished', # useless data
 'author_cakeday'] # useless data

# create list of unwanted columns from the post df
post_garbage_columns = [
 'author_flair_background_color', # useless data
 'author_flair_css_class', # useless data
 'author_flair_richtext', # useless data
 'author_flair_text', # useless data
 'author_flair_text_color', # useless data
 'author_flair_type', # useless data
 'author_fullname', # useless data
 'author_patreon_flair', # useless data
 'author_premium', # useless data
 'awarders',
 'can_mod_post', # useless data
 'contest_mode', # useless data
 'domain',
 'gildings',
 'is_crosspostable', # useless data
 'is_meta',
 'is_original_content', # useless data
 'is_reddit_media_domain', # useless data
 'is_robot_indexable', # useless data
 'is_robot_indexable', # useless data
 'is_self', # useless data
 'is_video', # useless data
 'link_flair_background_color', # useless data
 'link_flair_css_class', # useless data
 'link_flair_richtext', # useless data
 'link_flair_template_id', # useless data
 'link_flair_text', # useless data
 'link_flair_text_color', # useless data
 'link_flair_type', # useless data
 'locked', # useless data
 'media_only', # useless data
 'no_follow', # useless data
 'over_18',
 'parent_whitelist_status', # useless data
 'pinned', # useless data
 'pwls',
 'retrieved_on', # date this was added to pushshift, not useful
 'send_replies', # useless data
 'spoiler', # useless data
 'stickied', # useless data
 'subreddit', # only pulling from wsb, not helpful
 'subreddit_id', # only pulling from wsb, not helpful
 'subreddit_subscribers', # useless data
 'subreddit_type', # useless data
 'suggested_sort', # useless data
 'thumbnail', # useless data
 'treatment_tags', # useless data
 'whitelist_status', # useless data
 'wls', # useless data
 'removed_by_category', # useless data
 'post_hint', # useless data
 'preview', # useless data
 'thumbnail_height', # useless data
 'thumbnail_width', # useless data
 'url_overridden_by_dest', # useless data
 'media_metadata', # useless data
 'gallery_data', # useless data
 'is_gallery', # useless data
 'media', # useless data
 'media_embed', # useless data
 'secure_media', # useless data
 'secure_media_embed', # useless data
 'banned_by', # useless data
 'author_flair_template_id', # useless data
 'author_cakeday', # useless data
 'edited', # useless data
 'gilded', # useless data
 'distinguished', # useless data
 'collections', # useless data
 'crosspost_parent', # useless data
 'crosspost_parent_list', # useless data
 'allow_live_comments', # useless data
 'num_crossposts', # useless data
 'all_awardings' # useless data
 ]


# Drop all unwanted columns from both dataframes
clean_comment_df = cleaned_df.drop(comment_garbage_columns, 1)
clean_post_df = post_df.drop(post_garbage_columns,1)

# save the cleaned dfs to csv
# clean_post_df.to_csv("cleaned_wsb_posts.csv", index=False)
# clean_comment_df.to_csv("cleaned_wsb_comments.csv", index=False)