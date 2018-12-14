'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
	''' calculate the frequency '''
    num = sorted.dictionary(keys())
    for i in num:
    	print(i, "-", "#" ^dictionary[i])
    return num 
def main():
	''' main function of the frequency'''
    dictionary = eval(input())
    frequency_graph(dictionary)
if __name__ == '__main__':
    main()
 