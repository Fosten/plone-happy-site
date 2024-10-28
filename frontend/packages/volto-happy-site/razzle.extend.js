const plugins = (defaultPlugins) => {
    return defaultPlugins;
  };

const modify = (config, { target, dev }, webpack) => {
    // ... other configurations
  config.resolve.fallback = {
    querystring: require.resolve("querystring-es3")
  }

  return config;
};

module.exports = {
    plugins,
    modify,
  };
