<p>Search an array for the value "purple", and then replace it with "Blue".</p>

<?php
$arr = array("blue","red","green","yellow");
print_r(str_replace("red","Blue",$arr,$i));
echo "<br>" . "Replacements: $i";

#output : Search an array for the value "purple", and then replace it with "Blue". Array ( [0] => blue [1] => Blue [2] => green [3] => yellow ) 
Replacements: 1
