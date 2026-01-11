feed_back={"Positive": 45, "Neutral": 18, "Negative": 7}
total_feedback=sum(feed_back.values())
print(total_feedback)
max_type=max(feed_back.values())
print(max_type)
high_feedback_type=max(feed_back.keys())
print(high_feedback_type)
