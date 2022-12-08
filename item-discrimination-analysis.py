def item_discrimination_analysis(item_responses):
  """
  This function takes a list of responses to a multiple choice item and
  returns the item discrimination index.
  """
  num_students = len(item_responses)
  num_correct = sum([1 for response in item_responses if response == 1])
  percent_correct = num_correct / num_students

  # Calculate the average percentage of correct responses for the top and bottom
  # half of the students, based on their overall performance.
  sorted_students = sorted(item_responses, key=lambda x: x[1])
  num_students_top_half = num_students // 2
  num_students_bottom_half = num_students - num_students_top_half

  top_half_responses = sorted_students[:num_students_top_half]
  bottom_half_responses = sorted_students[num_students_top_half:]

  top_half_correct = sum([1 for response in top_half_responses if response == 1])
  bottom_half_correct = sum([1 for response in bottom_half_responses if response == 1])

  top_half_percent_correct = top_half_correct / num_students_top_half
  bottom_half_percent_correct = bottom_half_correct / num_students_bottom_half

  # Calculate the item discrimination index.
  item_discrimination_index = (top_half_percent_correct - bottom_half_percent_correct) / (1 - bottom_half_percent_correct)

  return item_discrimination_index
