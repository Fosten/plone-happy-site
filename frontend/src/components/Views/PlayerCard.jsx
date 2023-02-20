import React from "react";
import { DefaultView } from "@plone/volto/components";
import { Helmet } from '@plone/volto/helpers';
import { Container, Header, Image, Segment } from 'semantic-ui-react';
import { flattenToAppURL } from '@plone/volto/helpers';

const PlayerCardView = (props) => {
  const { content } = props;
  return (
      <Container>
      <div id="page-document">
      <Helmet title={content.title} />
      <h1 className="documentFirstHeading">
        {content.title}
      </h1>
      <Segment clearing>
      <Image
          src={flattenToAppURL(content.image?.scales?.preview?.download)}
          size="small"
          floated="right"
          alt={content.image_caption}
          avatar
        />
        <p>Birthdate: {content.birthdate}</p>
        <p>Positions: {content.positions}</p>
        <p>Current Team: {content.currentteam}</p>
      <div dangerouslySetInnerHTML={{ __html: content.blurb.data }} />
      </Segment>
      </div>
      </Container>
  );
};

export default PlayerCardView;