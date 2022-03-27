

function handle_menu() {
  let nav_Bar = document.querySelector('.nav-bar-bf4-800');

  nav_Bar.classList.toggle("navdisplay");    
}

// ########################################################################
// reload page 
// ########################################################################



// ########################################################################
// manipulate dom data (mainly topic) with ajax and view
// ########################################################################

function update_Tplist(subject,course,topics) {
  // $(".subj-topic-cl").empty();
  // console.log($(".subj-topic-cl"))
  // $(".subj-topic").text(subject+" :-")
  // topics.forEach(element => {
  //   ne_elm = `<li style="list-style: disc" class= "nowRenderthis" topic-id="${element["id"]}" >
  //       <a
  //         href='/${course}/${subject}/${element["name"]}'
  //         class="mrgn-auto"
  //       >
  //         ${element["name"]}
  //       </a>
  //     </li>`;
  //     $(".subj-topic-cl").append(ne_elm);
  // });

}


$(".iterate_subj_topics").click(function () {

  sb_id = $(this).attr("subj-id");
  sb_name = $(this).attr("subject-name");
  crc_name = $(".course-name").attr("course-name")
  // $.ajax({
  //   type: "GET",
  //   url: "/upd_sbj_tp/",
  //   data: {
  //     subj_id: sb_id,
  //   },
  //   dataType: "json",
  //   success: function (data) {
      
  //     update_Tplist(sb_name,crc_name,data["data"]);

  //   },
  //   error: function (data) {
  //     console.log(data, "fbsdf");
  //   },
  // });
});

// ##################################################################
// content in masonary grid
// ##################################################################

// function resizeGridItem(item){
//     grid = document.getElementsByClassName("masonary")[0];
//     rowHeight = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-auto-rows'));
//     rowGap = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-row-gap'));
//     rowSpan = Math.ceil((item.getBoundingClientRect().height+rowGap)/(rowHeight+rowGap));
//   item.style.gridRowEnd = "span " + rowSpan;
//   // console.log(item.getBoundingClientRect().height,rowGap,rowHeight,rowSpan);
//   }
  
//   function resizeAllGridItems(){
//     allItems = document.getElementsByClassName("content");
//     for(x=0;x<allItems.length;x++){
//       resizeGridItem(allItems[x]);
//     }
//   }
  
//   function resizeInstance(instance){
//     item = instance.elements[0];
//     resizeGridItem(item);
//   }
  
//   window.onload = resizeAllGridItems();
//   window.addEventListener("resize", resizeAllGridItems);
  


 