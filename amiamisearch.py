import amiami
import sys
#import multiprocessing

good_avail = ["Pre-order", "Pre-owned", "Limited", "On Sale", "Available"]

def get_info_on_search(search_ele, search_sort = "Price"):
    print("start search")
    results = amiami.searchPaginated(search_ele)
    csv_out = "Product,Price(JPY),Availability,URL\n"
    
    #iter = 0
    for item in results.items:
        # if iter:=iter+1 >= 10:
        #     break
        if(item.availability in good_avail):
            print(f"Product: {item.productName}, Price: {item.price}, Availability: {item.availability}, URL: {item.productURL}")
            csv_out += f"{item.productName},{item.price},{item.availability},{item.productURL}\n"
    
    return csv_out

def main(path = None):
    if not path:
        term = input("Please input a search term. ")
        out = get_info_on_search(term)
        with open(f"{term}_amiami.csv","w") as f:
            f.write(out)

    else:
        terms = []

        with open(path,"r") as f:
            for line in f:
                terms.append(line)
        
        for term in terms:
            out = get_info_on_search(term)
            with open(f"{term}_amiami.csv","w") as f:
                f.write(out)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()