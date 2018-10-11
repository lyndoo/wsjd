
export default {

  namespace: '命名空间',

  state: {
    data: [],       // 渲染用的order数据存在这里
    pagination: {   // 分页信息
      page: 1,
      pageSize: 10,
    },
    stores: [],     // 供用户选择的店铺列表在这里
  },

  subscriptions: {
    setup({ dispatch, history }) {  // 路由监听
      history.listen(({ pathname, query: { activityType } }) => {
        if (pathname === '/bossOrder') {
          dispatch({              //   这里会触发事件
            type: 'init',
            activityType,
          });
        }
      });
    },
  },
}