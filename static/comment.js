$('#new_comment_btn').click(function (e) {
    var token = $(this).data("token");
    var post_id = $(this).data("id");
    var comment = $("#id_comment").val();
    console.log('here!!!!')
    $.ajax({
      url: "/create_comment/",
      type: "POST",
      data: {
        post_id: post_id,
        body: comment,
        csrfmiddlewaretoken: token,
      },
      success: function (res) {
        if (res.bool == true) {
          $("#id_comment").val("");
          window.location.reload()
        }
      },
    });
    });