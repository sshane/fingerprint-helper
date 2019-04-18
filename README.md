# fingerprint-helper

fingerprint-helper is a useful tool for [openpilot](https://github.com/commaai/openpilot) designed to help you find similar already supported fingerprints, and merge your unsupported fingerprint.

Included is easy formatting from a Sentry error, where an `L` is following every value. It's automatically filtered out and converted to a dictionary for you.

The fingerprints in `fingerprints.py` is a collection of all fingerprints from [arne/openpilot](https://github.com/arne182/openpilot).

Example:

    >> find_matches('{384L: 8, 258L: 8, 1031L: 8, 264L: 8, 268L: 8, 653L: 8, 270L: 8, 792L: 8, 274L: 2, 660L: 8, 280L: 8, 284L: 8, 669L: 3, 671L: 8, 288L: 7, 290L: 6, 291L: 8, 292L: 8, 294L: 8, 168L: 8, 559L: 8, 520L: 8, 308L: 8, 564L: 8, 571L: 3, 320L: 8, 544L: 8, 331L: 8, 324L: 8, 680L: 8, 332L: 8, 514L: 8, 344L: 8, 770L: 8, 672L: 8, 800L: 8, 863L: 8, 736L: 8, 737L: 8, 746L: 5, 658L: 6, 368L: 8, 625L: 8, 500L: 8, 501L: 8, 760L: 8, 532L: 8, 764L: 8}')
    
    1. JEEP GRAND CHEROKEE V6 2018
    Exact matches: 80

    2. CHRYSLER PACIFICA HYBRID 2018
    Exact matches: 48

    3. CHRYSLER PACIFICA 2018
    Exact matches: 48

    4. CHRYSLER PACIFICA HYBRID 2017
    Exact matches: 47

    5. CHRYSLER PACIFICA HYBRID 2019
    Exact matches: 47

    Please enter the number next to the model you'd like to merge with: 5
    
    1 value mismatch to fix!

    Key: 564
    Your unsupported fingerprint value: 8
    Selected model fingerprint value: 1

    Please type value to use with merge: 1
    
    Sucessfully merged!

    1 changed key/value pairs added to fingerprint!
    
    >> {512: 8, 1024: 8, 514: 8, 515: 7, 516: 7, 517: 7, 518: 7, 1031: 8, 520: 8, 1033: 8, 1538: 8, 528: 8, 344: 8, 532: 8, 1050: 8, 943: 8, 542: 8, 1568: 8, 34: 35, 1059: 8, 557: 8, 559: 8, 560: 4, 564: 1, 54: 8, 1082: 8, 571: 3, 1025: 8, 584: 8, 1098: 8, 75: 9, 1100: 8, 1537: 8, 782: 8, 770: 8, 608: 8, 1026: 8, 624: 8, 625: 8, 632: 8, 639: 8, 704: 8, 2016: 8, 653: 8, 654: 8, 655: 8, 792: 8, 658: 6, 660: 8, 1562: 8, 671: 8, 672: 8, 678: 8, 168: 8, 701: 8, 1216: 8, 705: 8, 1218: 8, 1220: 8, 709: 8, 710: 8, 1225: 8, 501: 8, 719: 8, 720: 6, 1235: 8, 706: 8, 804: 8, 1242: 8, 1246: 8, 736: 8, 737: 8, 1250: 8, 746: 5, 680: 8, 764: 8, 766: 8, 469: 8, 257: 5, 258: 8, 1284: 8, 773: 8, 264: 8, 779: 8, 268: 8, 270: 8, 784: 8, 274: 2, 729: 5, 280: 8, 284: 8, 799: 8, 288: 7, 290: 6, 291: 8, 292: 8, 294: 8, 808: 8, 300: 8, 816: 8, 817: 8, 308: 8, 820: 8, 826: 8, 832: 8, 480: 8, 1858: 8, 324: 8, 838: 2, 1865: 8, 331: 8, 332: 8, 848: 8, 1875: 8, 853: 8, 983: 8, 825: 2, 856: 4, 1882: 8, 860: 6, 1886: 8, 863: 8, 1890: 8, 1083: 8, 1892: 8, 878: 8, 368: 8, 2024: 8, 882: 8, 376: 3, 384: 8, 897: 8, 388: 4, 908: 8, 320: 8, 1860: 8, 924: 3, 926: 3, 929: 8, 937: 8, 938: 8, 939: 8, 940: 8, 941: 8, 942: 8, 669: 3, 947: 8, 948: 8, 500: 8, 956: 8, 958: 8, 959: 8, 448: 6, 456: 4, 969: 4, 1856: 8, 974: 5, 464: 8, 760: 8, 979: 8, 980: 8, 981: 8, 982: 8, 544: 8, 984: 8, 800: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8}
