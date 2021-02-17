def busyStudent(startTime, endTime, queryTime):
    ans=0
    for i in range(len(startTime)):
        if startTime[i]<=queryTime and endTime[i]>queryTime:
            ans+=1

    print(ans)
    return ans



startTime=[1,2,3]
endTime=[3,2,7]
queryTime=4
busyStudent(startTime,endTime,queryTime)