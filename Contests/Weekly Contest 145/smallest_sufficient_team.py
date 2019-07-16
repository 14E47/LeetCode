class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        selected = []

        while len(req_skills)!= 0:
            maxx = 0
            index = None
            max_skills = []
            for i in people:
                skills_count = 0
                skills = []
                for j in i:
                    if j in req_skills:
                        skills_count += 1
                        skills.append(j)
                if skills_count > maxx:
                    maxx = skills_count
                    max_skills = skills
                    index = people.index(i)

            for i in max_skills:
                req_skills.pop(req_skills.index(i))

            selected.append(index)
        return sorted(selected)


req_skills = ["java","nodejs","reactjs"]
people = [["java"],["nodejs"],["nodejs","reactjs"]]
# Output: [0,2]
req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
# Output: [1,2]

c = Solution().smallestSufficientTeam(req_skills, people)
print(c)