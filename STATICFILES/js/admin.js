$(".email_log").blur(function () {
	if (!$(this).val()) {
		// console.log("white")
		$(this).next("#email_log").removeClass("form-lbcss-tg");
	} else {
		// console.log("black")
		$(this).next("#email_log").addClass("form-lbcss-tg");
	}
});

// ###############################################################
// ###############################################################
// dash board link css

if ($(".dash-side-bar").length) {
	var url_index;
	if ($(".dash-side-bar > ul > li").length > 4) {
		url_index = {
			admin_portal: 1,
			TopicSubjectCourse: 2,
			QuestionsReview: 3,
			QuestionAddAlter: 3,
			ArticlesReview: 4,
			ArticleAddAlter: 4,
			UserUploads: 5,
			MembersData: 7,
		};
	} else {
		url_index = {
			admin_portal: 1,
			QuestionsReview: 2,
			QuestionAddAlter: 2,
			ArticlesReview: 3,
			ArticleAddAlter: 3,
			UserUploads: 4,
		};
	}

	var ourpath = $(location).attr("href");
	ourpath = ourpath.split("/");
	var nav_index;
	if (url_index[ourpath[ourpath.length - 1]]) {
		nav_index = url_index[ourpath[ourpath.length - 1]];

		$(".dash-side-bar > ul")
			.children()
			.eq(nav_index - 1)
			.addClass("active-nav");
	} else if (url_index[ourpath[ourpath.length - 1].split("?")[0]]) {
		nav_index = url_index[ourpath[ourpath.length - 1].split("?")[0]];
		$(".dash-side-bar > ul")
			.children()
			.eq(nav_index - 1)
			.addClass("active-nav");
	} else if (url_index[ourpath[ourpath.length - 2]]) {
		nav_index = url_index[ourpath[ourpath.length - 2]];
		$(".dash-side-bar > ul > li")
			.eq(nav_index - 1)
			.addClass("active-nav");
	}
}

// ########################################################################
// below code is for dom manipulation to add course or topic we choose
// ########################################################################
function add_icos(e) {
	// console.log($(e).parent().attr('id'))
	$(e).removeAttr("onclick");
	var elem_parentid = $(e).parent().attr("id");
	if (elem_parentid == "cs_all") {
		content = `<span id="${$(e).attr("id")}">
		<i class="far fa-times-circle" onclick="remove_icos(this)" ></i>
		${$(e).text()}</span> `;

		$(".create-course-match-tags").append(content);
		$(`#id_Exam_Id > [value=${$(e).attr("id")}]`).attr("selected", "selected");
	}
	if (elem_parentid == "sb_all") {
		console.log($(e).attr("id"));
		content = `<span id="${$(e).attr("id")}">
		<i class="far fa-times-circle" onclick="remove_icos(this)" ></i>
		${$(e).text()}</span> `;
		$(".create-subjects-match-tags").append(content);
		$(`#id_Subj_Id > [value=${$(e).attr("id")}]`).attr("selected", "selected");
	}
	if (elem_parentid == "ts_all") {
		content = `<span id="${$(e).attr("id")}">
		<i class="far fa-times-circle" onclick="remove_icos(this)" ></i>
		${$(e).text()}</span> `;

		$(".create-topics-match-tags").append(content);
		$(`#id_Topic_Id > [value=${$(e).attr("id")}]`).attr("selected", "selected");
	}
	if (elem_parentid == "tgs_all") {
		content = `<span id="${$(e).attr("id")}">
		<i class="far fa-times-circle" onclick="remove_icos(this)" ></i>
		${$(e).text()}</span> `;

		$(".create-tags-match-tags").append(content);
		$(`#id_Tag_Id > [value=${$(e).attr("id")}]`).attr("selected", "selected");
	}
}
// ########################################################################
// below code is for dom manipulation to delete parent element and
// create course or topics item attribute again so that icos can add again
// ########################################################################
function remove_icos(e) {
	var elem_parentclass = $(e).parent().parent().attr("class");
	console.log(elem_parentclass);
	if (elem_parentclass == "create-course-match-tags") {
		$(`#cs_all > #${$(e).parent().attr("id")}`).attr(
			"onclick",
			"add_icos(this)"
		);
		$(`#id_Exam_Id > [value=${$(e).parent().attr("id")}]`).removeAttr(
			"selected"
		);
	}
	if (elem_parentclass == "create-subjects-match-tags") {
		$(`#sb_all > #${$(e).parent().attr("id")}`).attr(
			"onclick",
			"add_icos(this)"
		);
		$(`#id_Subj_Id > [value=${$(e).parent().attr("id")}]`).removeAttr(
			"selected"
		);
	}
	if (elem_parentclass == "create-topics-match-tags") {
		$(`#ts_all > #${$(e).parent().attr("id")}`).attr(
			"onclick",
			"add_icos(this)"
		);
		$(`#id_Topic_Id > [value=${$(e).parent().attr("id")}]`).removeAttr(
			"selected"
		);
	}
	if (elem_parentclass == "create-tags-match-tags") {
		$(`#tgs_all > #${$(e).parent().attr("id")}`).attr(
			"onclick",
			"add_icos(this)"
		);
		$(`#id_Tag_Id > [value=${$(e).parent().attr("id")}]`).removeAttr(
			"selected"
		);
	}
	$(e).parent().remove();
}

// ###############################################################################################
// below code for show topics and course with search pattern in
// Questions and article fields
// ###############################################################################################
var allDataCS_TP; // very important variable

function for_updateQuestionorArticle() {
	// ##########################################################################################
	// ##########################################################################################
	// below code is for Questions admin panel

	// field is for exam_Id or cource_Id for Questions
	if ($("#id_Exam_Id > [selected]").length) {
		$.each($("#id_Exam_Id > [selected]"), (index, value) => {
			content = `<span id="${$(value).attr("value")}">
				<i class="far fa-times-circle" onclick="remove_icos(this)" ></i>
				${$(value).text()}</span> `;

			$(".create-course-match-tags").append(content);
			$(`#id_Exam_Id > [value=${$(value).attr("value")}]`).attr(
				"selected",
				"selected"
			);
			$(`#cs_all > #${$(value).attr("value")}`).removeAttr("onclick");
		});
	}
	// field is for Topics_Id for Questions and CST
	if ($("#id_Topic_Id > [selected]").length) {
		$.each($("#id_Topic_Id > [selected]"), (index, value) => {
			content = `<span id="${$(value).attr("value")}">
				<i class="far fa-times-circle" onclick="remove_icos(this)" ></i>
				${$(value).text()}</span> `;

			$(".create-topics-match-tags").append(content);
			$(`#id_Topic_Id > [value=${$(value).attr("value")}]`).attr(
				"selected",
				"selected"
			);
			$(`#ts_all > #${$(value).attr("value")}`).removeAttr("onclick");
		});
	}
	// ############################################################################################
	// ############################################################################################

	// <----------------------------seprator------------------------------------------------------>

	// ############################################################################################
	// ############################################################################################
	// below code is for Articles admin panel

	if ($("#id_Tag_Id > [selected]").length) {
		$.each($("#id_Tag_Id > [selected]"), (index, value) => {
			content = `<span id="${$(value).attr("value")}">
				<i class="far fa-times-circle" onclick="remove_icos(this)" ></i>
				${$(value).text()}</span> `;
			$(".create-tags-match-tags").append(content);
			$(`#id_Tag_Id > [value=${$(value).attr("value")}]`).attr(
				"selected",
				"selected"
			);
			$(`#tgs_all > #${$(value).attr("value")}`).removeAttr("onclick");
		});
	}
	// ############################################################################################
	// ############################################################################################

	// field is for Subj_Id for CST
	if ($("#id_Subj_Id > [selected]").length) {
		$.each($("#id_Subj_Id > [selected]"), (index, value) => {
			content = `<span id="${$(value).attr("value")}">
				<i class="far fa-times-circle" onclick="remove_icos(this)" ></i>
				${$(value).text()}</span> `;

			$(".create-subjects-match-tags").append(content);
			$(`#id_Subj_Id > [value=${$(value).attr("value")}]`).attr(
				"selected",
				"selected"
			);
			$(`#sb_all > #${$(value).attr("value")}`).removeAttr("onclick");
		});
	}
}

function makefields(fieldata, creator_id) {
	// ##########################################################################################
	// ##########################################################################################
	// below code is for Questions admin panel

	if ($(".Question-add-form").length) {
		$(`#id_Creater_Id > [value=${creator_id}]`).attr("selected", "selected");
		Object.entries(fieldata[0]).map((key, i) => {
			content = `<li class="slct-course" id="${key[1]}" onclick="add_icos(this)">${key[0]}</li>`;
			$("#cs_all").append(content);
		});
		Object.entries(fieldata[1]).map((key, i) => {
			content = `<li class="slct-topic" id="${key[1]}" onclick="add_icos(this)">${key[0]}</li>`;
			$("#ts_all").append(content);
		});
	}

	// ############################################################################################
	// ############################################################################################

	// <----------------------------seprator------------------------------------------------------>

	// ############################################################################################
	// ############################################################################################
	// below code is for CST admin panel
	if ($(".cst-add-form").length) {
		Object.entries(fieldata[1]).map((key, i) => {
			content = `<li class="slct-topic" id="${key[1]}" onclick="add_icos(this)">${key[0]}</li>`;
			$("#ts_all").append(content);
		});
		Object.entries(fieldata[2]).map((key, i) => {
			content = `<li class="slct-sbjs" id="${key[1]}" onclick="add_icos(this)">${key[0]}</li>`;
			$("#sb_all").append(content);
		});
	}

	// ############################################################################################
	// ############################################################################################

	// <----------------------------seprator------------------------------------------------------>

	// ############################################################################################
	// ############################################################################################
	// below code is for Articles admin panel
	if ($(".Article-add-form").length) {
		$(`#id_Creater_Id > [value=${creator_id}]`).attr("selected", "selected");
		Object.entries(fieldata[0]).map((key, i) => {
			content = `<li class="slct-tags" id="${key[1]}" onclick="add_icos(this)">${key[0]}</li>`;
			$("#tgs_all").append(content);
		});
	}

	// ############################################################################################
	// ############################################################################################

	// <----------------------------seprator------------------------------------------------------>

	// ############################################################################################
	// below is for both
	if (
		$("#id_Exam_Id > [selected]") ||
		$("#id_Topic_Id > [selected]") ||
		$("#id_Tag_Id > [selected]")
	) {
		for_updateQuestionorArticle();
	}
}

// here we are getting all the topics and course
if ($(".Question-add-form").length || $(".cst-add-form").length) {
	$.ajax({
		type: "GET",
		url: "/admin_portal/Courses_Topics_Tags_all/",
		dataType: "json",
		data: {
			data: "cstp",
		},
		success: function (data) {
			// console.log(data);
			// this is global variable we use to
			// manipulate courses and topics data
			allDataCS_TP = data["data"];
			console.log(data["data"]);
			// below function was to create list for both courses and topics
			makefields(allDataCS_TP, data["user"]);
		},
		error: function (error) {
			console.log(error);
		},
	});
}
// here we are getting all the tags
if ($(".Article-add-form").length) {
	console.log();

	$.ajax({
		type: "GET",
		url: "/admin_portal/Courses_Topics_Tags_all/",
		dataType: "json",
		data: {
			data: "tg",
		},
		success: function (data) {
			// console.log(data);
			// this is global variable we use to
			// manipulate courses and topics data
			allDataCS_TP = data["data"];
			console.log(data["data"]);
			// below function was to create list for both courses and topics
			makefields(allDataCS_TP, data["user"]);
		},
		error: function (error) {
			console.log(error);
		},
	});
}

// this function is for if the value math exist
// return that and load courses and topic
function checkDataExist(check, value) {
	let create_elm_list = [];

	// ##########################################################################################
	// ##########################################################################################
	// below code is for Questions admin panel

	if (check == "for-courses-type") {
		Object.entries(allDataCS_TP[0]).map((key, i) => {
			key[0].toLowerCase().indexOf(value.toLowerCase()) > -1
				? create_elm_list.push(key)
				: "";
		});
		$("#cs_all").empty();
		create_elm_list.forEach((element) => {
			onclick_statement = $(`.create-course-match-tags > #${element[1]}`).length
				? ""
				: 'onclick="add_icos(this)"';
			content = `<li class="slct-course" id="${element[1]}" ${onclick_statement}>${element[0]}</li>`;
			$("#cs_all").append(content);
		});
	} else if (check == "for-topics-type") {
		Object.entries(allDataCS_TP[1]).map((key, i) => {
			key[0].toLowerCase().indexOf(value.toLowerCase()) > -1
				? create_elm_list.push(key)
				: "";
		});
		$("#ts_all").empty();
		create_elm_list.forEach((element) => {
			onclick_statement = $(`.create-topics-match-tags > #${element[1]}`).length
				? ""
				: 'onclick="add_icos(this)"';
			content = `<li class="slct-topic" id="${element[1]}" ${onclick_statement}>${element[0]}</li>`;
			$("#ts_all").append(content);
		});
	}
	// ############################################################################################
	// ############################################################################################

	// <----------------------------seprator------------------------------------------------------>

	// ############################################################################################
	// ############################################################################################
	// below code is for CST admin panel
	else if (check == "for-subjects-type") {
		Object.entries(allDataCS_TP[2]).map((key, i) => {
			key[0].toLowerCase().indexOf(value.toLowerCase()) > -1
				? create_elm_list.push(key)
				: "";
		});
		$("#sb_all").empty();
		create_elm_list.forEach((element) => {
			onclick_statement = $(`.create-subjects-match-tags > #${element[1]}`)
				.length
				? ""
				: 'onclick="add_icos(this)"';
			content = `<li class="slct-sbjs" id="${element[1]}" ${onclick_statement}>${element[0]}</li>`;
			$("#sb_all").append(content);
		});
	}

	// ############################################################################################
	// ############################################################################################

	// <----------------------------seprator------------------------------------------------------>

	// ############################################################################################
	// ############################################################################################
	// below code is for Articles admin panel
	else if (check == "for-tags-type") {
		Object.entries(allDataCS_TP[0]).map((key, i) => {
			key[0].toLowerCase().indexOf(value.toLowerCase()) > -1
				? create_elm_list.push(key)
				: "";
		});
		$("#tgs_all").empty();
		create_elm_list.forEach((element) => {
			onclick_statement = $(`.create-tags-match-tags > #${element[1]}`).length
				? ""
				: 'onclick="add_icos(this)"';
			content = `<li class="slct-tags" id="${element[1]}" ${onclick_statement}>${element[0]}</li>`;
			$("#tgs_all").append(content);
		});
	}

	// ############################################################################################
	// ############################################################################################
}

// in this function we are going to change the
// courses or topics to value inside thier input field
$(".check_data_Nalter").keyup(function (e) {
	e.preventDefault();
	// console.log($(this).val())
	checkDataExist($(this).attr("id"), $(this).val());
});
