from API import TalkPythonAPI
import webbrowser

def main():
    kw = input('Enter a search term: ')
    # Get results from TalkPythonApi.py
    results = TalkPythonAPI.get_search_result(kw)
    cnt = 0
    for r in results:
        cnt +=1
        # Print the (named tuples) results
        print(f'{cnt}. {r.title}')
    # Select the index and open the url in browser
    choice = int(input('Which would you like to visit?')) - 1
    webbrowser.open('talkpython.fm' + results[choice].url)

if __name__ == '__main__':
    main()
