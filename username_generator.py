import argparse
import textwrap

class UserGen:
    
    def __init__(self, args):
        self.args = args

    def full_name_w_peroid(self, names):
        name = names.replace(' ', '.').strip()
        return name

    def first_initial_last_name(self, names):
        name = names.split(' ')[0][0:1].strip() + names.split(' ')[1].strip()
        return name

    def first_last_initial(self, names):
        name = names.split(' ')[0].strip() + names.split(' ')[1][0:1].strip()
        return name

    def first_initial_peroid_last_name(self, names):
        name = names.split(' ')[0][0:1].strip() + '.' + names.split(' ')[1].strip()
        return name

    def first_last(self, names):
        name = names.replace(' ', '').strip()
        return name

    def last_name(self, names):
        name = names.split(' ')[1].strip()
        return name

    def first_dash_last(self, names):
        name = names.replace(' ', '-').strip()
        return name

    def first_underscore_last(self, names):
        name = names.replace(' ', '_').strip()
        return name
    
    def last_first(self, names):
        name = names.split(' ')[1].strip() + names.split(' ')[0].strip()
        return name
    
    def last_first_initial(self, names):
        name = names.split(' ')[1].strip() + names.split(' ')[0][0:1].strip()
        return name
    
    def generate_name_list(self):
        try:
            with open(self.args.input, 'r') as source:
                with open(self.args.output, 'w+') as target:
                    lines = source.readlines()
                    for line in lines:
                        target.write(self.first_underscore_last(line.strip())+'\n')
                        target.write(self.first_dash_last(line.strip())+'\n')
                        target.write(self.first_initial_last_name(line.strip())+'\n')
                        target.write(self.first_initial_peroid_last_name(line.strip())+'\n')
                        target.write(self.first_last(line.strip())+'\n')
                        target.write(self.first_last_initial(line.strip())+'\n')
                        target.write(self.full_name_w_peroid(line.strip())+'\n')
                        target.write(self.last_name(line.strip())+'\n')
                        target.write(self.last_first(line.strip())+'\n')
                        target.write(self.last_first_initial(line.strip())+'\n')
        except IndexError:
            print("""
Please make sure the input file is a first and last name separated by a space.
ex. John Smith
            """)
            exit()
        except FileNotFoundError:
            print("The input file was not found, please double check the path and name of the input.")
            exit()

    def generate_name_list_email(self):
        email = '@' + self.args.email
        try:
            with open(self.args.input, 'r') as source:
                with open(self.args.output, 'w+') as target:
                    lines = source.readlines()
                    for line in lines:
                        target.write(self.first_underscore_last(line.strip())+email+'\n')
                        target.write(self.first_dash_last(line.strip())+email+'\n')
                        target.write(self.first_initial_last_name(line.strip())+email+'\n')
                        target.write(self.first_initial_peroid_last_name(line.strip())+email+'\n')
                        target.write(self.first_last(line.strip())+email+'\n')
                        target.write(self.first_last_initial(line.strip())+email+'\n')
                        target.write(self.full_name_w_peroid(line.strip())+email+'\n')
                        target.write(self.last_name(line.strip())+email+'\n')
                        target.write(self.last_first(line.strip())+email+'\n')
                        target.write(self.last_first_initial(line.strip())+email+'\n')    
        except IndexError:
            print("""
Please make sure the input file is a first and last name separated by a space.
ex. John Smith
            """)
            exit()
        except FileNotFoundError:
            print("The input file was not found, please double check the path and name of the input.")
            exit()

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(
    description = 'Username Generator',
        
    formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
                                Example: username_generator.py -i <username list> -o <output file> -e <email>
                                Example: username_generator.py -i username.txt -o generated_names.txt -e example.com
                               ''')
    )
    
    parser.add_argument('-i', '--input', help='Path/Name of input file', required=True)
    parser.add_argument('-o', '--output', default='generated_names.txt', help='Path/Name of desired output file')
    parser.add_argument('-e', '--email', help='Add email address to usernames')
    
    args = parser.parse_args()

    ug = UserGen(args)
    
    if (args.email):
        ug.generate_name_list_email()
    else:
        ug.generate_name_list()
        
    