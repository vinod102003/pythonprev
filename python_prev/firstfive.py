with open(file_path, 'r') as file:
            lines = file.readlines()
            
            # Display the first 5 lines
            print("First 5 lines:")
            for line in lines[:5]:
                print(line, end='')
            
            print("\n" + "="*40 + "\n")
            
            # Display the last 5 lines
            print("Last 5 lines:")
            for line in lines[-5:]:
                print(line, end='')