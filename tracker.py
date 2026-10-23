
import urllib.request
import re

PRODUCT_NAME = "Twinings Pure Peppermint Tea Bags"
PRODUCT_URL = "https://www.woolworths.com.au/shop/productdetails/888487/twinings-pure-peppermint-tea-bags"

def main():
    print("Checking Woolworths...")
    print(f"Product: {PRODUCT_NAME}")

    request = urllib.request.Request(
        PRODUCT_URL,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            page = response.read().decode("utf-8", errors="replace")

        print(f"Page downloaded: {len(page)} characters")

        # Look for price-like values near the product ID.
        matches = re.findall(r'.{0,80}888487.{0,150}', page)

        if matches:
            print("Found information near the product ID:")
            for match in matches[:5]:
                print(match[:230])
        else:
            print("Product ID not found in page source.")

        prices = re.findall(
            r'\$\s?\d{1,4}\.\d{2}',
            page
        )

        print(f"Price-like values found: {len(prices)}")
        print("First price-like values:", prices[:15])

    except Exception as error:
        print(f"Could not retrieve the page: {error}")

if __name__ == "__main__":
    main()
