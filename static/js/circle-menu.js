function CircleMenu(args) {
    var _this = this;
    var _menu = args.menu || []
    this.menu = [].concat(args.menu).concat(args.menu);
    this.wrap = document.getElementById(args.wrap);
    this.circle = document.getElementById(args.circle);
    this.direction = args.direction || 0;
    this.division = this.menu.length;
    // 验证转动方向是否合法
    CircleMenu.directionCheck(this.direction);
    this.speed = args.speed || 1;
    // 检测速率参数是否合法
    CircleMenu.speedCheck(this.speed);
    var start = 0;
    var rotate = 0;
    var _rotate = 0;
    var maxAngle = CircleMenu.maxAngle(this.menu.length, this.division);

    function touchHandler(e, type) {
        var touch = e.changedTouches[0];
        var circle = this.circle;
        switch (type) {
            case 'start':
                start = touch.clientY;
                break;
            case 'end':
                var _rotate = 0
                if (this.direction === 1) {
                    _rotate = CircleMenu.distanceY(start, touch.clientY, this.wrap, this.speed) + rotate;
                } else if (this.direction === 0) {
                    _rotate = (CircleMenu.distanceY(start, touch.clientY, this.wrap, this.speed) - rotate) * (-1);
                }
                start = 0;
                // if (this.direction === 1 && (_rotate > 0 || Math.abs(_rotate) >= maxAngle)) {
                //     if (_rotate > 0) {
                //         rotate = 0
                //     } else if (Math.abs(_rotate) >= maxAngle) {
                //         rotate = maxAngle * (-1);
                //     }
                // } else if (this.direction === 0 && (_rotate < 0 || Math.abs(_rotate) >= maxAngle)) {
                //     if (_rotate < 0) {
                //         rotate = 0
                //     } else if (_rotate >= maxAngle) {
                //         rotate = maxAngle;
                //     }
                // } else {
                //     rotate = _rotate;
                // }
                rotate = _rotate;
                
                if (Math.abs(rotate) > 360) {
                    rotate %= 360;
                }
                break;
            case 'move':
                e.preventDefault(); // 防止移动设备浏览器屏幕上下滑动 
                var nextRotate = 0;
                if (this.direction === 1) {
                    nextRotate = CircleMenu.distanceY(start, touch.clientY, this.wrap, this.speed) + rotate;
                } else if (this.direction === 0) {
                    nextRotate = (CircleMenu.distanceY(start, touch.clientY, this.wrap, this.speed) - rotate) * (-1);
                }
                // if (this.direction === 1 && (nextRotate > 0 || Math.abs(nextRotate) > maxAngle)) {
                //     // 超越极限范围, 不转动, 未来可以在此做缓冲逻辑
                //     if (nextRotate > 0) {
                //         // console.log('move-nextRotate > 0', nextRotate > 0, nextRotate);
                //     } else if (Math.abs(nextRotate) > maxAngle) {
                //         // console.log(
                //         //     'move-Math.abs(nextRotate) > maxAngle',
                //         //     Math.abs(nextRotate) >= maxAngle,
                //         //     nextRotate,
                //         // );
                //     }
                // } else if (this.direction === 0 && (nextRotate < 0 || nextRotate > maxAngle)) {
                //     // 超越极限范围, 不转动
                //     if (nextRotate < 0) {
                //         // console.log('* move nextRotate < 0: ', nextRotate);
                //     } else if (nextRotate > maxAngle) {
                //         // console.log('* move nextRotate > maxAngle: ', nextRotate);
                //     }
                // } else {
                //     // console.log('+ move', nextRotate, rotate)
                //     // circle.style.transform = 'rotate(' + nextRotate + 'deg)';
                // }
                circle.style.transform = 'rotate(' + nextRotate + 'deg)';
                break;
        }
    }

    // 先检测DOM元素是否存在
    if (!this.wrap) {
        CircleMenu.domError(args.wrap);
    }
    if (!this.circle) {
        CircleMenu.domError(args.circle);
    }
    // 开始设置根容器的样式
    CircleMenu.setStyle(this.wrap, {
        position: 'relative',
        height: '100%',
        width: '100%',
        overflow: 'hidden',
        background: '#324471 url("/static/img/bg' + this.direction + '.jpg") no-repeat ' + (this.direction ? '0' : '100%') + ' center',
        backgroundSize: '100% auto'
    });
    var _r = CircleMenu.circleRadius(this.wrap);
    CircleMenu.setStyle(this.circle, {
        height: _r * 2 + 'px',
        width: _r * 2 + 'px',
        position: 'absolute',
        top: 0,
        left: this.direction === 1 ? 0 : '100%',
        margin: ((_r * 2 - this.wrap.offsetHeight) / (-2)) + 'px 0 0 ' + (_r * (-1)) + 'px',
        transform: 'rotate(' + rotate + 'deg)'
    });

    // 渲染菜单
    CircleMenu.renderMenu(this.menu, this.circle, this.division, this.direction);

    // 监听根容器元素的touch事件
    this.wrap.addEventListener("touchstart", function (e) {
        touchHandler.call(_this, e, 'start')
    }, false);
    this.wrap.addEventListener("touchmove", function (e) {
        touchHandler.call(_this, e, 'move')
    }, false);
    this.wrap.addEventListener("touchend", function (e) {
        touchHandler.call(_this, e, 'end')
    }, false);

}

CircleMenu.distanceY = function (a, b, wrap, speed) {
    var res = b - a;
    var height = wrap.offsetHeight;
    return (res / height) * (speed || 1) * 180;;
};
CircleMenu.domError = function (id) {
    throw new Error('DOM元素 "#' + id + '" 不存在, 你是不是写错了id名称?')
};
CircleMenu.directionCheck = function (direction) {
    if (direction !== 0 && direction !== 1) {
        throw new Error('当前direction值是 ' + direction + ' , 此值必须是0 或者 1, 默认0')
    }
};
CircleMenu.speedCheck = function (speed) {
    if (speed <= 0 || speed > 3) {
        throw new Error('转动速率参数-speed必须介于0 和 3中间, 当前为 ' + speed + ' 倍速')
    }
};
CircleMenu.setStyle = function (dom, styles) {
    if (!dom) {
        throw new Error('目标DOM不存在');
    }
    if (typeof styles !== 'object') {
        throw new Error('参数styles应该是个object类型的值!!');
    }
    for (var sk in styles) {
        if (styles.hasOwnProperty(sk)) {
            dom.style[sk] = styles[sk];
        }
    }
    return dom;
};
CircleMenu.circleRadius = function (wrap, rate) {
    return wrap.offsetWidth * (rate || .9);
};
CircleMenu.maxAngle = function (len, division) {
    var totle = 360 / division * len;
    if (totle <= 180) {
        return false; // 不可以转动
    }
    if (totle > 180 && totle <= 360) {
        return totle - 180;
    }
};
CircleMenu.renderMenu = function (data, target, division, direction) {
    if (!target) {
        throw new Error('目标宿主容器DOM不存在');
    }
    if (data && (Array.isArray && !Array.isArray(data))) {
        throw new Error('data参数的值必须是数组!');
    }
    if (typeof division !== 'number' || division < 6 || division > 30) {
        throw new Error('division是等分圆周的份数, 必须是数字, 介于5~30份, 太少不好看, 太多更不好看');
    }
    var origin = target.offsetHeight / 2; // 原点位置, 旋转半径
    var unitDeg = 360 / division; // 每份的角度
    var width = Math.PI * origin * 2 / division * 0.7;
    var height = origin / 2;
    var linkHeight = height / 2;
    var fontSize = height / 12;
    data.map(function (item, i) {
        // 创建单个按钮元素
        var btn = document.createElement('a');
        CircleMenu.setStyle(btn, {
            position: 'absolute',
            display: 'block',
            color: '#fff',
            width: width + 'px',
            height: height + 'px',
            textAlign: 'center',
            marginLeft: (width / (-2)) + 'px',
            marginTop: (height / (-2)) + 'px'
        });
        btn.setAttribute('href', item.url);
        // 创建文字 shiyong
        // var txt = document.createElement('canvas');
        // CircleMenu.setStyle(txt, {
        //     position: 'absolute',
        //     top: 0,
        //     left: 0,
        //     // height: '50px',
        //     backgroundColor: '#f00',
        //     opacity: .5
        // });
        // txt.setAttribute('width', width);
        // txt.setAttribute('height', linkHeight);
        // var ctx = txt.getContext('2d');
        // var sPoint = [(width - fontSize * 4) / 2, (linkHeight + fontSize) / 2];
        // var cPoint = [width / 2, 0];
        // var ePoint = [(width + fontSize * 4) / 2, (linkHeight + fontSize) / 2];
        // ctx.beginPath();
        // ctx.moveTo(sPoint[0], sPoint[1]);
        // ctx.arcTo(cPoint[0], cPoint[1], ePoint[0], ePoint[1], 70);
        // ctx.arc(
        //     width / 2,
        //     origin,
        //     origin - ((linkHeight + fontSize) / 2),
        //     0,
        //     Math.PI,
        //     true
        // );
        // 路径曲线可以绘制, 但是没有内置方法可以绘制跟对曲线的文字, 图森破
        // 换个思路, 使用 css 算每个字的坐标的转动角度
        // ctx.arc(
        //     width / 2,
        //     origin,
        //     origin - ((linkHeight + fontSize) / 2),
        //     Math.PI * (0.6 / division + 0.5) * (-1),
        //     Math.PI * (0.5 - 0.6 / division) * (-1),
        //     false
        // );
        // ctx.strokeStyle = 'yellow';
        // ctx.lineWidth = 3;
        // ctx.stroke();

        var txt = document.createElement('span');
        CircleMenu.setStyle(txt, {
            position: 'relative',
            color: '#fff',
            fontSize: fontSize + 'px',
            textDecoration: 'none',
            display: 'block',
            width: width + 'px',
            height: linkHeight + 'px',
            textShadow: '0 3px 30px #99ccff',
            top:'-10px'
            // backgroundColor: '#f00',
            // opacity: 0.5
        })
        var len = item.name.length
        var textAngle = (len * fontSize / width) * unitDeg / len;
        var topFix = (height / 2 - fontSize) / 2;
        var isOdd = len % 2 !== 0
        var halfIndex = Math.floor(len / 2);
        var topRatio = -2;
        var leftRatio = 0.3 ;
        var leftFix = (width  - (((len - 1) * leftRatio + len) * fontSize)) / 2;
        for (var ti = 0; ti < len; ti++) {
            var t = document.createElement('b');
            var tStyle = {
                position: 'absolute',
                display: 'block',
                height: fontSize + 'px',
                width: fontSize + 'px',
                fontWeight: 'normal',
                left: (leftFix + fontSize * (ti + (ti * (ti === 0 ? 0 : leftRatio)))) + 'px',
                transform: 'rotate(' + textAngle * (halfIndex - ti - 0.5) * (-1) +'deg)',
            }
            if ((ti + 1) <= halfIndex) {
                tStyle.top = (topFix + (ti * topRatio)) + 'px';
            } else {
                tStyle.top = (topFix + ((len - ti - 1) * topRatio)) + 'px';
            }

            CircleMenu.setStyle(t, tStyle)
            t.innerText = item.name[ti]
            txt.appendChild(t)
        }

        // 创建链接元素
        // var btnLink = document.createElement('span');
        // btnLink.className = 'btnLink';
        // // btnLink.innerHTML = item.name;
        // CircleMenu.setStyle(btnLink, {
        //     position: 'relative',
        //     color: '#fff',
        //     fontSize: fontSize + 'px',
        //     textDecoration: 'none',
        //     display: 'block',
        //     width: width + 'px',
        //     height: linkHeight + 'px',
        //     // lineHeight: linkHeight + 'px',
        //     textAlign: 'center'
        // });
        // btnLink.appendChild(txt);
        btn.appendChild(txt);

        // 创建图标元素
        var img = document.createElement('div');
        CircleMenu.setStyle(img, {
            fontSize: (height / 8 + 10) + 'px',
            display: 'block',
            width: width + 'px',
            height: linkHeight + 'px',
            lineHeight: linkHeight + 'px',
            textAlign: 'center',
            position: 'relative',
            left: '-4px'
        });
        var imgRes = document.createElement('img');
        imgRes.setAttribute('src', item.ico);
        imgRes.setAttribute('alt', item.name);
        CircleMenu.setStyle(imgRes, {
            height: (height / 4 - 5) + 'px'
        });
        img.appendChild(imgRes);
        btn.appendChild(img);

        // 添加分割线
        var line = document.createElement('div');
        CircleMenu.setStyle(line, {
            position: 'absolute',
            right: 0,
            top: '-2%',
            display: 'block',
            width: 0,
            height: '100%',
            borderLeft: '2px solid #fff',
            opacity: 0.2,
            transform: 'rotate(' + (180 / division) + 'deg)'
        });

        btn.appendChild(line);
        // 向中心缩进的系数是 0.72
        var _rate = 0.72;
        var _x = i + 0.5; // 偏移半个单位的量
        var deg = (((unitDeg * _x) + 90) * Math.PI) / 180;
        var top = (origin - (Math.sin(deg) * origin * _rate)) + 'px';
        var left = (origin - (Math.cos(deg) * origin * _rate)) + 'px';
        var rotate = unitDeg * _x;
        if (direction === 0) {
            left = (origin + (Math.cos(deg) * origin * _rate)) + 'px';
            rotate = unitDeg * _x * (-1);
        }
        CircleMenu.setStyle(btn, {
            position: 'absolute',
            top: top,
            left: left,
            transform: 'rotate(' + rotate + 'deg)'
        });
        target.appendChild(btn);
    });
};