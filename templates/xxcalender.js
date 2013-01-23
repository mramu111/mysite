<script language="javascript">
<!--
// fill the month table with column headings
function day_title(day_name){
     document.write("<TD ALIGN=center WIDTH=35>"+day_name+"</TD>")
}
// fills the month table with numbers
function fill_table(month,month_length)
{ 
  day=1
  // begin the new month table
  document.write("<TABLE BORDER=3 CELLSPACING=3 CELLPADDING=%3><TR>")
  document.write("<TD COLSPAN=7 ALIGN=center><B>"+month+"   "+year+"</B><TR>")
  // column headings
  day_title("Sun")
  day_title("Mon")
  day_title("Tue")
  day_title("Wed")
  day_title("Thu")
  day_title("Fri")
  day_title("Sat")
  // pad cells before first day of month
  document.write("</TR><TR>")
  for (var i=1;i<start_day;i++){
        document.write("<TD>")
  }
  // fill the first week of days
  for (var i=start_day;i<8;i++){
        document.write("<TD ALIGN=center>"+day+"</TD>")
        day++
  }
  document.write("<TR>")
  // fill the remaining weeks
  while (day <= month_length) {
     for (var i=1;i<=7 && day<=month_length;i++){
         document.write("<TD ALIGN=center>"+day+"</TD>")
         day++
     }
     document.write("</TR><TR>")
     // the first day of the next month
     start_day=i
  }
  document.write("</TR></TABLE><BR>")
}
// end hiding -->

</script>
<script language="javascript">
<!--
// fill the month table with column headings
function day_title(day_name){
     document.write("<TD ALIGN=center WIDTH=35>"+day_name+"</TD>")
}
// fills the month table with numbers
function fill_table(month,month_length)
{ 
  day=1
  // begin the new month table
  document.write("<TABLE BORDER=3 CELLSPACING=3 CELLPADDING=%3><TR>")
  document.write("<TD COLSPAN=7 ALIGN=center><B>"+month+"   "+year+"</B><TR>")
  // column headings
  day_title("Sun")
  day_title("Mon")
  day_title("Tue")
  day_title("Wed")
  day_title("Thu")
  day_title("Fri")
  day_title("Sat")
  // pad cells before first day of month
  document.write("</TR><TR>")
  for (var i=1;i<start_day;i++){
        document.write("<TD>")
  }
  // fill the first week of days
  for (var i=start_day;i<8;i++){
        document.write("<TD ALIGN=center>"+day+"</TD>")
        day++
  }
  document.write("<TR>")
  // fill the remaining weeks
  while (day <= month_length) {
     for (var i=1;i<=7 && day<=month_length;i++){
         document.write("<TD ALIGN=center>"+day+"</TD>")
         day++
     }
     document.write("</TR><TR>")
     // the first day of the next month
     start_day=i
  }
  document.write("</TR></TABLE><BR>")
}
// end hiding -->

</script>
