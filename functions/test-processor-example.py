p1 = [("task-1", 4),
      ("task-2", 7),
      ("task-3", 3),
      ("task-4", 9)
      ]

p2 = [("task-1", 2),
      ("task-2", 7),
      ("task-3", 3),
      ("task-4", 2)
      ]

processors = [("p1", p1),
              ("p2", p2)
              ]
low_time = 0
fast_processor = None

for processor_name, processor_object in processors:
    for task, duration in processor_object:
        print("{} - {}".format(task, duration))
        if low_time == 0:
            low_time = duration
            fast_processor = processor_name
        elif duration <= low_time:
            low_time = duration
            fast_processor = processor_name
        else:
            continue

print("Faster processor is {} and lowest time is {}".format(fast_processor, low_time))
