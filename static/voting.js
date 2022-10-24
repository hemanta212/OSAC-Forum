$(document).ready(function () {
  $(".downvote-click").click(function () {
    var post_id = $(this).data("id");
    var token = $(this).data("token");
    var type = $(this).data("type");
    $.ajax({
      url: "/downvote/",
      type: "POST",
      data: {
        post_id: post_id,
        type: type,
        csrfmiddlewaretoken: token,
      },
      success: function (res) {
        //Right now, the vote-count is increased or decreased onclick
        //But malfunctions when a user swithces from upvote to downvote or vice versa

        if (res.bool == true) {
          if (type == "comment") {
            var _vote_count = $(".comment-vote-count-" + post_id).text();
            $(".comment-vote-count-" + post_id).text(parseInt(_vote_count) - 1);
            if (
              $(".downvote-click-comment[data-id=" + post_id + "]").val() ==
              "Downvote"
            ) {
              $(".downvote-click-comment[data-id=" + post_id + "]").val(
                "Downvoted"
              );
              if (
                $(".upvote-click-comment[data-id=" + post_id + "]").val() ==
                "Upvoted"
              ) {
                $(".upvote-click-comment[data-id=" + post_id + "]").val(
                  "Upvote"
                );
              }
            } else {
              $(".downvote-click-comment[data-id=" + post_id + "]").val(
                "Downvote"
              );
            }
          } else {
            var _vote_count = $(".vote-count-" + post_id).text();
            $(".vote-count-" + post_id).text(parseInt(_vote_count) - 1);
            if (
              $(".downvote-click[data-id=" + post_id + "]").val() == "Downvote"
            ) {
              $(".downvote-click[data-id=" + post_id + "]").val("Downvoted");
              if (
                $(".upvote-click[data-id=" + post_id + "]").val() == "Upvoted"
              ) {
                $(".upvote-click[data-id=" + post_id + "]").val("Upvote");
              }
            } else {
              $(".downvote-click[data-id=" + post_id + "]").val("Downvote");
            }
          }
        }
      },
    });
  });

  $(".upvote-click").click(function () {
    var token = $(this).data("token");
    var post_id = $(this).data("id");
    var type = $(this).data("type");
    $.ajax({
      url: "/upvote/",
      type: "POST",
      data: {
        post_id: post_id,
        type: type,
        csrfmiddlewaretoken: token,
      },
      success: function (res) {
        if (res.bool == true) {
          if (type == "comment") {
            var _vote_count = $(".comment-vote-count-" + post_id).text();

            $(".comment-vote-count-" + post_id).text(parseInt(_vote_count) + 1);
            if (
              $(".upvote-click-comment[data-id=" + post_id + "]").val() ==
              "Upvote"
            ) {
              $(".upvote-click-comment[data-id=" + post_id + "]").val(
                "Upvoted"
              );
              if (
                $(".downvote-click-comment[data-id=" + post_id + "]").val() ==
                "Downvoted"
              ) {
                $(".downvote-click-comment[data-id=" + post_id + "]").val(
                  "Downvote"
                );
              }
            }
          } else {
            var _vote_count = $(".vote-count-" + post_id).text();
            $(".vote-count-" + post_id).text(parseInt(_vote_count) + 1);
            if (
              $(".upvote-click-post[data-id=" + post_id + "]").val() == "Upvote"
            ) {
              $(".upvote-click-post[data-id=" + post_id + "]").val("Upvoted");
              if (
                $(".downvote-click-post[data-id=" + post_id + "]").val() ==
                "Downvoted"
              ) {
                $(".downvote-click-post[data-id=" + post_id + "]").val(
                  "Downvote"
                );
              }
            } else {
              $(".upvote-click-post[data-id=" + post_id + "]").val("Upvote");
            }
          }
        }
      },
    });
  });
});
