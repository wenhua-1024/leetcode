public class leetcode_8 {
    public int myAtoi(String str) {
        str = str.trim();
          if (str.length() > 0) {
              char c = str.charAt(0);
              String reg = "\\D+";
              String[] strs;
              if (c == '+' || c == '-') {
                  str = str.substring(1);
              }
              if ((strs = str.split(reg)).length == 0 || "".equals(strs[0])) return 0;
              try {
                  return c == '-' ? -Integer.parseInt(strs[0]) : Integer.parseInt(strs[0]);
              } catch (Exception e) {
                  return c == '-' ? Integer.MIN_VALUE : Integer.MAX_VALUE;
              }
          }
          return 0;
      }
}
