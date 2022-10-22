$('#new_comment_btn').click(function (e) {
    var token = $(this).data("token");
    var post_id = $('#id_comment').data("id");
    var comment = $("#id_comment").val();
    console.log(post_id)
    console.log(comment)
    console.log('here!!!!')
    $.ajax({
      url: "http://127.0.0.1:8000/create_comment/", //have to edit this
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