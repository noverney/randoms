import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Setup Your Account',
    Svg: require('@site/static/img/SVG/question.svg').default,
    description: (
      <>
        Ever played &apos;Guess Who?&apos; with your colleagues? Dive into Meeting Munch and discover teammates hiding in plain sight!
      </>
    ),
  },
  {
    title: 'Choose Your Preferences',
    Svg: require('@site/static/img/SVG/interpersonal.svg').default,
    description: (
      <>
        Less than 5 quick questions and bam! You&apos;re set up with a mystery colleague. Who knew office intros could feel like a game show?
      </>
    ),
  },
  {
    title: 'Meet in Real Life',
    Svg: require('@site/static/img/SVG/icebreaker.svg').default,
    description: (
      <>
        Need a convo starter? We&apos;ve got you covered! Kick things off with a quirky fun fact about your new pal. Chatting has never been this fun!
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
