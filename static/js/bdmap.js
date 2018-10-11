function searchMap(address,city)
{
    var map = new BMap.Map("container");
    map.centerAndZoom(new BMap.Point(113.649, 34.756), 11);
    map.enableScrollWheelZoom(true);
    var ls = new BMap.LocalSearch(map,{renderOptions:{map:map},pageCapacity:1});
    //ls.setPageCapacity(100);
    ls.search(address,{forceLocal:true});
}