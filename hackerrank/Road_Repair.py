# Road Repair

import os

def getMinCost(crew_id, job_id):
    distance = 0
    crew_id.sort()
    job_id.sort()

    for idx in range(len(crew_id)):
        set_distance = job_id[idx] - crew_id[idx]
        if set_distance < 0:
            print("here")
            set_distance *= -1
        distance += set_distance

    return distance


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crew_id_count = int(input().strip())

    crew_id = []

    for _ in range(crew_id_count):
        crew_id_item = int(input().strip())
        crew_id.append(crew_id_item)

    job_id_count = int(input().strip())

    job_id = []

    for _ in range(job_id_count):
        job_id_item = int(input().strip())
        job_id.append(job_id_item)

    result = getMinCost(crew_id, job_id)

    fptr.write(str(result) + '\n')

    fptr.close()
