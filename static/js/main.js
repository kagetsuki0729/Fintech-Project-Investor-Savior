$(function () {
    $("#start-query").click(function (event) { // 當此按鈕被點擊
        event.preventDefault();
        var keywords = $("#query-text-field").val()
        var gtrendChart = "<script type=\"text/javascript\"> trends.embed.renderExploreWidget(\"TIMESERIES\", {\"comparisonItem\":[{\"keyword\":\""
        gtrendChart += keywords
        gtrendChart += "\",\"geo\":\"US\",\"time\":\"today 12-m\"}],\"category\":0,\"property\":\"\"}, {\"exploreQuery\":\"q="
        gtrendChart+=keywords.replace(/ /g,"%20")
        gtrendChart += "&geo=US&date=today 12-m\",\"guestPath\":\"https://trends.google.com:443/trends/embed/\"}); <"
        gtrendChart+="\/script>"
        //console.log(gtrendChart)
        $("#gtrend").contents().find('body').html(gtrendChart)
        return false
    });
});