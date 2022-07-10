const customerAuth = async (ctx, next) => {
    const authorization = ctx.get('Authorization');
    const token = authorization.replace('Bearer ', '');
    console.log('pasando por middleware auth')

    try {
        const user = await ctx.db.jugador.findOne({
        where: {
          token,
        },
      });

      if (user) {
        ctx.currentUser = user;
        return next(ctx);
      } else {
        ctx.body = { error: 'Debes iniciar sesión' };
      }
    } catch (error) {
      return (ctx.body = { error: 'Debes iniciar sesión' });
    }
  };

  module.exports = customerAuth;
