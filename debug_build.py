import traceback
try:
    import build_i18n
    build_i18n.main()
    with open('C:/Users/Admin/WorkBuddy/2026-07-07-14-01-01/dbg.txt', 'w', encoding='ascii', errors='replace') as f:
        f.write('OK build finished\n')
except Exception:
    with open('C:/Users/Admin/WorkBuddy/2026-07-07-14-01-01/dbg.txt', 'w', encoding='ascii', errors='replace') as f:
        f.write(traceback.format_exc())
