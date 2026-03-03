def any_arrows(arrows):
    for arrow in arrows:
         if not arrow.get("damaged", False):
              return True
    return False