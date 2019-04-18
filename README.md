# fingerprint-helper

fingerprint-helper is a useful tool for openpilot designed to help you find similar already supported fingerprints, and merge your unsupported fingerprint.

Included is easy formatting from a Sentry error, where an `L` is following every value. It's automatically filtered out and converted to a dictionary for you.

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
