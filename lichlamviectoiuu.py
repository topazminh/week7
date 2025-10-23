# Mỗi công việc có (bắt đầu, kết thúc, lợi ích)
jobs = [(1, 3, 50), (3, 5, 20), (6, 9, 100), (2, 8, 200)]

def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])  # sắp theo thời gian kết thúc
    n = len(jobs)
    dp = [0]*n

    def last_non_conflict(i):
        for j in range(i-1, -1, -1):
            if jobs[j][1] <= jobs[i][0]:
                return j
        return -1

    dp[0] = jobs[0][2]
    for i in range(1, n):
        incl = jobs[i][2]
        l = last_non_conflict(i)
        if l != -1:
            incl += dp[l]
        dp[i] = max(incl, dp[i-1])
    return dp[-1]

print("Tổng lợi ích tối đa:", job_scheduling(jobs))
