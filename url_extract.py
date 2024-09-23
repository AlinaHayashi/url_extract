import re
import csv

def extract_urls_from_file(input_file):
    url_pattern = r'https?://[^\s]+'
    urls = set()
    
    with open(input_file, 'r') as file:
        for line in file:
            found_urls = re.findall(url_pattern, line)
            urls.update(found_urls)
    
    return list(urls)

def write_urls_to_csv(urls, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        url_writer = csv.writer(csvfile)
        for url in urls:
            url_writer.writerow([url])

def main():
    input_file = 'input.txt'
    output_file = 'output.csv'
    
    urls = extract_urls_from_file(input_file)
    
    if urls:
        write_urls_to_csv(urls, output_file)
        print(f'Extracted {len(urls)} unique URLs and saved to {output_file}.')
    else:
        print('ERROR No URLs found.')
    
    input("Press enter to exit...")

if __name__ == "__main__":
    main()
