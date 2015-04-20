var battles = [
    [1, 'url1', 'New York, USA', 'battle1'],
    [2, 'url2', 'Boston, USA', 'battle2'],
    [3, 'url3', 'Sydney, Australia', 'battle3'],
    [4, 'url4', 'Shanghai, China', 'battle4'],
    [5, 'url5', 'London, UK', 'battle5']
];

var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 1,
    center: new google.maps.LatLng(0, 0),
    mapTypeId: google.maps.MapTypeId.ROADMAP
});

var infowindow = new google.maps.InfoWindow({
    content: "content"
});

function setcontent(marker, x) {
    infowindow.setContent('<div id="content">' +
        '<h1 id="firstHeading" class="firstHeading">' + battles[x][2] + '</h1>' +
        '<div id="bodyContent">' +
        '<p>' + battles[x][3] + '</p>' +
        '<p>Videolink: <a href="https://www.tinyurl.com/' + battles[x][1] + '">' +
        'https://www.tinyurl.com/' + battles[x][1] + '</a></p>' +
        '</div>' +
        '</div>');
}

var j = 0;

for (var x = 0; x < battles.length; x++) {

    $.getJSON('http://maps.googleapis.com/maps/api/geocode/json?address=' + battles[x][2] + '&sensor=false', null, function (data, i) {
        var ite = j;
        j++;
        var p = data.results[0].geometry.location;
        var latlng = new google.maps.LatLng(p.lat, p.lng);
        var marker = new google.maps.Marker({
            position: latlng,
            map: map
        });


        google.maps.event.addListener(marker, 'click', (function (marker) {
            return function () {
                setcontent(marker, ite);
                infowindow.open(map, marker);
            }
        })(marker, i));
    });
}