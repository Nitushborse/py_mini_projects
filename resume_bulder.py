def collect_input() -> dict:
    name = input("Enter your name :: ").strip()
    qualification = input("Enter your qualification:: ").strip()
    skills = input("Enter your skills by comma sepereted :: ").strip().split(',')
    project= input("Enter your project name and detail :: ").strip().split(',')

    userInfo = {
        "name" : name,
        "qualification": qualification,
        "skills" : skills,
        "project":project
    }

    return userInfo



def create_resume(userInfo:dict):

    with open(f"{userInfo['name']}.txt","w") as f:
        for key, value in userInfo.items():
            f.write(f"{key}:{value}\n")

def display_resume(resume):
    with open(resume, "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)
    

# data = collect_input()
# create_resume(data)
# display_resume("bhavesh")

def main():
    data = collect_input()
    create_resume(data)
    print(f"\nThis is your resume {data['name']}!")
    display_resume(f"{data['name']}.txt")
    

main()
